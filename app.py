from flask import Flask, render_template, request, jsonify
from comment_sunburst import generate_sunburst_chart
import sqlite3
import os
import shutil
from flask import send_from_directory

# Database functions
def insert_video_chart_info(video_title, chart_path):
    """Insert video information into database"""
    conn = sqlite3.connect('video.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO VideoChart (video_title, chart_path)
        VALUES (?, ?)
    ''', (video_title, chart_path))
    conn.commit()
    conn.close()

def clear_table():
    """Clear all records from VideoChart table"""
    conn = sqlite3.connect('video.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM VideoChart")
    conn.commit()
    conn.close()

def clear_output_folder():
    """Clear all files in final_output folder"""
    folder_path = 'final_output'
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        os.makedirs(folder_path)  # Recreate the empty folder



# Flask application
app = Flask(__name__)

@app.route('/get_video_data', methods=['GET'])
def get_video_data():
    """Fetch video data from the database for display in the table."""
    conn = sqlite3.connect('video.db')
    cursor = conn.cursor()
    cursor.execute("SELECT video_title, chart_path FROM VideoChart")
    videos = cursor.fetchall()
    conn.close()

    # Format data for JSON response
    video_data = [{'video_title': title, 'chart_path': path} for title, path in videos]
    return jsonify(video_data)


@app.route('/')
def index():
    return render_template('index.html')

# Route to serve files from the final_output folder
@app.route('/final_output/<path:filename>')
def serve_file(filename):
    return send_from_directory('final_output', filename)


@app.route('/generate', methods=['POST'])
def generate_chart():
    youtube_link = request.form.get('youtube_link')
    video_title, chart_path = generate_sunburst_chart(youtube_link)
    insert_video_chart_info(video_title, chart_path)
    
    # Return JSON response to indicate success
    return jsonify({'success': True, 'chart_path': chart_path})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    """Clear database and output folder"""
    try:
        clear_table()            # Clear VideoChart table
        clear_output_folder()     # Clear files in final_output folder
        return jsonify({'success': True})
    except Exception as e:
        print("Error clearing history:", e)
        return jsonify({'success': False}), 500

if __name__ == '__main__':
    app.run(debug=True)
