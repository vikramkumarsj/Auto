
!pip install http://h2o-release.s3.amazonaws.com/h2o/rel-vapnik/1/Python/h2o-3.12.0.1-py2.py3-none-any.whl

import h2o
from h2o.automl import H2OAutoML

h2o.init()

df = h2o.import_file('D:/Data/prostate.csv')


train, test = df.split_frame(ratios=[.9])   

# Identify predictors and response
x = train.columns
y = "CAPSULE"
x.remove(y)

# For binary classification, response should be a factor
train[y] = train[y].asfactor()
test[y] = test[y].asfactor()
     
# Run AutoML for 60 seconds
aml = H2OAutoML(max_runtime_secs = 60)
aml.train(x = x, y = y, training_frame = train, leaderboard_frame = test)     


# View the AutoML Leaderboard
aml.leaderboard
aml.leader


preds = aml.predict(test)

preds[0]


preds = aml.leader.predict(test)

options("datatable.verbose"=TRUE)
pred2 = as.data.frame(perf)

dir(preds)

pred2 =  preds.as_data_frame()

data <- as.data.table(prediction = preds.predict[,0])

h2o.shutdown()





