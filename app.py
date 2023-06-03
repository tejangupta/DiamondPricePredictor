from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from src.logger import logging

application = Flask(__name__)
app = application


@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()

        logging.info('Starting prediction...')
        pred = predict_pipeline.predict(final_new_data)
        logging.info('Prediction completed.')

        estimated_price = round(pred[0], 2)
        logging.info(f'Estimated Price: {estimated_price}')

        return jsonify(estimated_price)


if __name__ == '__main__':
    app.run(debug=True)
