                         END-TO-END ARCHITECTURE

                    DATA SCIENCE / ML DEVELOPMENT
                               |
                               v
                    +-----------------------+
                    |    Google Colab       |
                    |                       |
                    | Data Preparation      |
                    | EDA                   |
                    | Feature Engineering   |
                    | Model Training        |
                    | Model Evaluation      |
                    +-----------+-----------+
                                |
                                | Model Artifacts
                                v
                    +-----------------------+
                    |      GitHub Repo      |
                    |                       |
                    | Notebook              |
                    | Model (.pkl)          |
                    | Metadata (.json)      |
                    | FastAPI               |
                    | Streamlit             |
                    | Dockerfile            |
                    | Requirements          |
                    +-----------+-----------+
                                |
                                | Project Deployment
                                v
                  +--------------------------------+
                  |        AWS EC2 - Ubuntu         |
                  |                                |
                  |       Docker Runtime           |
                  |              |                 |
                  |      +-------+--------+        |
                  |      |                |        |
                  |      v                v        |
                  |  +---------+    +-----------+  |
                  |  | FastAPI |    | Streamlit |  |
                  |  | :8000   |    |   :8501   |  |
                  |  +----+----+    +-----+-----+  |
                  |       |               |        |
                  |       v               v        |
                  |   ML Inference    Dataset      |
                  |   /predict        Upload       |
                  |       |               |        |
                  |       |               v        |
                  |       |             EDA         |
                  |       |               |        |
                  |       |               v        |
                  |       |          ML Prediction |
                  |       |               |        |
                  |       |               v        |
                  |       |          Monitoring    |
                  |       |               |        |
                  |       |               v        |
                  |       |          CSV Export    |
                  |       |                        |
                  +-------+------------------------+
                          |
                          v
                    EC2 Security Group
                     TCP 8000 / 8501
                          |
                          v
                    User Web Browser
