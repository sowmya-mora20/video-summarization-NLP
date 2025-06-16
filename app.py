from flask import Flask, request, jsonify, send_from_directory
from youtube_transcript_api import YouTubeTranscriptApi
from summa.summarizer import summarize
from googletrans import Translator
from urllib.parse import urlparse, parse_qs
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')
@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js')
@app.route('/summary', methods=['GET'])
def summary_api():
    try:
        url = request.args.get('url', '')
        lang = request.args.get('lang', 'en')
        length = request.args.get('length', 'medium')
        if not url:
            return jsonify({'error': 'Please provide a YouTube video URL'}), 400
        video_id = extract_video_id(url)
        if not video_id:
            return jsonify({'error': 'Invalid YouTube video URL'}), 400
        transcript_text, auto_generated = get_transcript(video_id)
        # Summarize
        summary = summarize(transcript_text) if not auto_generated else transcript_text[:5000]
        words = summary.split()
        percentages = {"small": 0.5, "medium": 0.7, "large": 1.0}
        percentage = percentages.get(length, 0.7)
        summary = ' '.join(words[:int(len(words) * percentage)])
        # Translate
        translator = Translator()
        translated_summary = translator.translate(summary, dest=lang).text
        return jsonify({'summary': translated_summary}), 200
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500
def extract_video_id(url):
    parsed_url = urlparse(url)
    if 'youtu.be' in parsed_url.netloc:
        return parsed_url.path.lstrip('/')
    query = parse_qs(parsed_url.query)
    return query.get('v', [None])[0]
def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])
        # DEBUG: print the first snippet type to verify structure
        first_snippet = next(iter(transcript.fetch()), None)
        print("First snippet type:", type(first_snippet))
        print("First snippet content:", first_snippet)
        # Access text attribute correctly
        text = ' '.join([snippet.text for snippet in transcript.fetch()])
        return text, transcript.is_generated
    except Exception as e:
        raise Exception(f'Transcript error: {str(e)}')
if __name__ == '__main__':
    app.run(debug=True)
