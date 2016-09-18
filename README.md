# Banyan_Hack - Crop per field prediction 

This site demonstrates a predictive model of crop yield in various districts of India. 

The implementation of the machine learning algorithm is done on azureML platform. We have used two datasets which are available in data.gov.in which provides a complete insight to different topological distribution in India.
We have mapped different crop with their respective seasons and also production of crop over different regions of state.
We take yield as a metric to categorize the maximum production of the crop. Yield is calculated as

                Y(i) =  Production(in tons) / Area (Hectares)

We've tested the prediction values using various algorithms for better results. Boosted Tree Decision Algorithm is used in this experiment. Webservice endpoints are created for accessing the service and predicting future values. The same is used for creating a web application which can be used by farmers to get accurate predictions.

#How It Works

Run the flask server which opens a dashboard. You can enter the values for Year, State, District and Season to get the predicted yield from the trained model. Relevant visualizations like state wise crop predictions have been added to the site.
