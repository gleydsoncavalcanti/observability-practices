# Cost Explorer metrics in the Prometheus
 This is a simple practice about exporter to collect metrics from Cost Explorer.
 
 Was develepor a template in kubernetes and a exporter in Python to metrics collect daily data of Cost Explorer.
 
 ## Requirements 
 * IAM Policy to cost explorer
 
   Example 
  ``` 
  {
           "Effect": "Allow",
           "Action": [
                "ce:*"
            ],
            "Resource": "*"
   } 
   ```
  * Cluster Kubernetes
  
  #### Exporter Deploy
  
  Create Namespace in Kubernetes 
  
  ``` kubectl create namespace aws-services ```
  
  We go application deploy
  
  ``` kubectl create -f aws-cost-explorer.yml ```
  
  The Metrics will can be visualized after deploy, in http://<your-ip>:9999
  
  ![image](https://user-images.githubusercontent.com/23400555/190505888-b4d946a0-5ed3-4ade-b88b-95d5bd0da7da.png)
