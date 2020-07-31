from flask import Flask, request, jsonify
admission_controller = Flask(__name__)
@admission_controller.route('/validate/deployments', methods=['POST'])
def deployment_webhook():
    request_info = request.get_json()    
    if request_info["request"]["object"]["metadata"]["labels"].get("osconf"):
        return admission_response(True, "osconf label exists")  
    return admission_response(False, "Not allowed without osconf label")
def admission_response(allowed, message):
    return jsonify({"response": {"allowed": allowed, "status": {"message": message}}})
if __name__ == '__main__':
    admission_controller.run(host='0.0.0.0', port=443, ssl_context=("/certs/tls.crt", "/certs/tls.key"))