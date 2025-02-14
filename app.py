from flask import Flask, request, jsonify, render_template, session
import os
from openai import OpenAI

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Initialize OpenAI client (or Dashscope)
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # Ensure you have the API key in your environment
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']

    # Retrieve previous messages from the session or initialize if none exist
    if 'messages' not in session:
        session['messages'] = [{'role': 'user', 'content': '你好'}]

    # Add user message to conversation history
    session['messages'].append({'role': 'user', 'content': user_message})

    # Call the API with the entire conversation history
    try:
        completion = client.chat.completions.create(
            model="deepseek-r1",  # Change model as needed
            messages=session['messages']
        )

        assistant_message = completion.choices[0].message.content
        reasoning_content = completion.choices[0].message.reasoning_content

        # Append assistant response to the conversation history
        session['messages'].append({'role': 'assistant', 'content': assistant_message})

        # Return the assistant's message, reasoning, and full conversation history for the frontend
        return jsonify({
            'assistant_message': assistant_message,
            'reasoning_content': reasoning_content,
            'messages': session['messages']
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)

