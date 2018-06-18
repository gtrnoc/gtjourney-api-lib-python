# gtjourney-api-lib-python
A library of Python packages to support creating web APIs for GT Journey.

#### This repo is mirrored
This repository is [homed on Georgia Tech's GitHub Enterprise](https://github.gatech.edu/gtjourney/gtjourney-api-lib-python)
and [mirrored to GitHub.com](https://github.com/gtrnoc/gtjourney-api-lib-python) to allow anonymous installation
via `pip` (GitHub Enterprise disallows anonymous git access).  Please use the GT GitHub Enterprise for development.

Updates to the GT GitHub Enterprise `master` branch should be manually pushed to GitHub.com.  There is no automatic
synchronization.

## Provided packages

###  flask_wso2apim_auth

Flask extension providing handling of user and app auth from WSO2 API Manager.  Provides function decorators to enforce
auth and retrieve end-user attributes from JSON Web Tokens for endpoints that require auth at the API Manager.  Has
additional support for Georgia Tech GT Accounts.

For more information on WSO2 API Manager support for passing auth data to the API backend, see the WSO2 API Manager
documentation: https://docs.wso2.com/display/AM210/Passing+Enduser+Attributes+to+the+Backend+Using+JWT
