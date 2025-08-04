
<h2>About This Project</h2>
<p>
  The <strong>AI-Powered Healthcare Intelligence Network</strong> is a cutting-edge platform that leverages Machine Learning (ML) and Natural Language Processing (NLP) to provide 
  accurate disease predictions, personalized medical recommendations, and AI-assisted drug suggestions. The system aims to enhance early diagnosis, reduce medical errors, and 
  offer intelligent healthcare solutions.
</p>
<h2>Features</h2>

<h3>Disease Prediction & Medical Recommendation</h3>
<p>
  This module uses <strong>Machine Learning</strong> to predict diseases based on symptoms and suggest the best medical recommendations.
</p>
<ul>
  <li>Predicts diseases based on symptoms provided by the user.</li>
  <li>Uses <strong>RandomForest Classifier</strong> for predictions.</li>
  <li>Provides recommended treatments and precautions.</li>
  <li>Provides medical descriptions, precautions, medication suggestions, and diet recommendations**.</li>
</ul>

<h3>AI-Powered Drug Recommendation</h3>
<p>
  Our AI system uses <strong>NLP & Cosine Similarity</strong> to recommend alternative medicines based on drug properties.
</p>
<ul>
  <li>AI-powered alternative medicine finder.</li>
   <li>Utilizes **NLP & cosine similarity** for **accurate drug matching**</li>
  <li>Matches medicines with similar ingredients.</li>
  <li>Ensures safer and more effective drug prescriptions.</li>
</ul>




<h3>Heart Disease Risk Assessment</h3>
<p>
  This module uses <strong>LightGBM & AI classifiers</strong> to assess heart disease risks based on patient history.
</p>
<ul>
  <li>Evaluates heart disease risk based on lifestyle and medical history.</li>
  <li>Uses machine learning models (LightGBM, EasyEnsemble) for predicting heart disease risk.  </li>
  <li>Takes inputs like age, BMI, smoking habits, medical history, etc.</li>
  <li>Provides a **personalized heart risk score with AI-driven recommendations**</li>
</ul>

<h3>Medibot - AI Health Assistant</h3>
<p>
  Our <strong>LLM-powered chatbot</strong> answers medical queries and provides instant healthcare insights using <strong>Hugging Face LLM (Mistral-7B-Instruct)</strong>.
</p>
<ul>
  <li>AI-powered medical chatbot based on Mistral-7B-Instruct.</li>
  <li>Retrieves medical information from a FAISS vector database.</li>
  <li>Retrieves reliable medical information using RAG (Retrieval Augmented Generation.</li>
  <li>Provides fast, relevant, and fact-based healthcare responses.</li>
  <li>Provides <strong>reliable AI-driven</strong> answers to health-related questions.</li>
</ul>

<h2>⚙️ Installation & Setup</h2>

<h3>Clone the Repository</h3>
<pre>
cd AI-Healthcare
</pre>

<h3>2Set Up the Virtual Environment</h3>
<pre>
python -m venv venv
venv\Scripts\activate  # On Windows
</pre>

<h3>Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>Set Up Environment Variables</h3>
<p>Create a <code>.env</code> file and add:</p>
<pre>
HF_TOKEN=your_huggingface_api_token
</pre>
<h3>5Run the Application</h3>
<pre>
streamlit run home.py
</pre>


" target="_blank">🔗 LinkedIn</a> |
  <a href="https://x.com/AbhaySingh71711" target="_blank"> 🐦 Twitter</a>
</p>
