# Machine Learning Film Recommendor Web App using Streamlit 

## Example use 


https://github.com/user-attachments/assets/0e613ba5-259c-496e-bd5d-6c5ca01933ed


## Information 

The recommendation service is powered using vector mathematics. We use the scikit Learn Countvectorizer class to extract relevant features
from a dataset of films, which are the genre and description.

These features are then learnt, and the document-term matrix is returned using the fit_transform method. The cosine similarity of the matrix was 
found to find a model where similar films had a smaller number and less similar ones had a larger number.

