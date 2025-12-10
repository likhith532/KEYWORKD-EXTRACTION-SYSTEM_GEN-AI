"""
Keyword Extraction System - Flask Backend
Domain: Journalism/Research
Models: KeyBERT, YAKE, RAKE, Ensemble
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import json
import time

# Import the extractor module
from model.extractor import KeywordExtractor

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
CORS(app)

# Initialize the keyword extractor
print("🔄 Loading Keyword Extraction Models...")
extractor = KeywordExtractor(config_path='model/config.json')
print("✅ Models loaded successfully!")


@app.route('/')
def index():
    """Serve the main frontend page"""
    return render_template('index.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Keyword Extraction API is running',
        'models': ['keybert', 'yake', 'rake', 'ensemble']
    })


@app.route('/api/extract', methods=['POST'])
def extract_keywords():
    """
    Extract keywords from text
    
    Request JSON:
    {
        "text": "Your text here...",
        "method": "ensemble",  // Options: keybert, yake, rake, ensemble
        "top_n": 10,
        "diversity": 0.5  // For KeyBERT only
    }
    
    Response JSON:
    {
        "success": true,
        "method": "ensemble",
        "keywords": [
            {"keyword": "example", "score": 0.95},
            ...
        ],
        "processing_time": 0.5
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'No text provided'
            }), 400
        
        text = data['text'].strip()
        if len(text) < 10:
            return jsonify({
                'success': False,
                'error': 'Text too short. Please provide at least 10 characters.'
            }), 400
        
        method = data.get('method', 'ensemble').lower()
        top_n = min(int(data.get('top_n', 10)), 50)  # Cap at 50
        diversity = float(data.get('diversity', 0.5))
        
        # Validate method
        valid_methods = ['keybert', 'yake', 'rake', 'ensemble']
        if method not in valid_methods:
            method = 'ensemble'
        
        # Extract keywords
        start_time = time.time()
        
        if method == 'yake':
            keywords = extractor.extract(text, top_n=top_n)
        elif method == 'keybert':
            keywords = extractor.extract(text, top_n=top_n)
        elif method == 'rake':
            keywords = extractor.extract(text, top_n=top_n)
        else:  # ensemble
            keywords = extractor.extract(text, top_n=top_n)
        
        processing_time = round(time.time() - start_time, 3)
        
        # Format response
        formatted_keywords = [
            {'keyword': kw, 'score': score} 
            for kw, score in keywords
        ]
        
        return jsonify({
            'success': True,
            'method': method,
            'keywords': formatted_keywords,
            'count': len(formatted_keywords),
            'processing_time': processing_time
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/extract/all', methods=['POST'])
def extract_all_methods():
    """
    Extract keywords using all methods for comparison
    
    Request JSON:
    {
        "text": "Your text here...",
        "top_n": 10
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'No text provided'
            }), 400
        
        text = data['text'].strip()
        top_n = min(int(data.get('top_n', 10)), 30)
        
        start_time = time.time()
        
        results = {
            'yake': [{'keyword': kw, 'score': score} for kw, score in extractor.extract(text, top_n=top_n)],
        }
        
        processing_time = round(time.time() - start_time, 3)
        
        return jsonify({
            'success': True,
            'results': results,
            'processing_time': processing_time
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/models', methods=['GET'])
def get_models_info():
    """Get information about available models"""
    return jsonify({
        'models': [
            {
                'id': 'yake',
                'name': 'YAKE',
                'description': 'Statistical keyword extraction - Lightweight & Fast',
                'best_for': 'Fast extraction, no GPU needed',
                'speed': 'Very Fast'
            }
        ]
    })


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"""
    ╔══════════════════════════════════════════════════════════╗
    ║     🔑 Keyword Extraction System - Backend Server        ║
    ╠══════════════════════════════════════════════════════════╣
    ║  🌐 Running on: http://localhost:{port}                    ║
    ║  📚 Domain: Journalism/Research                          ║
    ║  🤖 Models: KeyBERT, YAKE, RAKE, Ensemble               ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)
