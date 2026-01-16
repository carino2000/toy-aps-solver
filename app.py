import time

from flask import Flask, request
from scheduler.solver import solver_job_scheduler as solve_job
app = Flask(__name__)


@app.route('/api/solve', methods=['POST'])
def job_simulation_solver():
    data = request.get_json()
    resp = solve_job(data)

    time.sleep(len(resp["timeline"]) / 7)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
