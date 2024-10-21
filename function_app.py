import azure.functions as func
import logging
import openai
import os

# Ensure to have the OpenAI API key or relevant API key for your LLM package
# openai.api_key = "YOUR_OPENAI_API_KEY"
openai.api_key=os.environ['MYOPENAI']
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request with LLM.')

    user_input = req.params.get('input')
    if not user_input:
        return func.HttpResponse("Please pass an input query n the query string.", status_code=400)

    # Generate response using OpenAI or other LLMs
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=100
        )
        return func.HttpResponse(response.choices[0].text.strip(), mimetype="application/json")
    except Exception as e:
        logging.error(f"Error during LLM processing: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)


