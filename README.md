# 🏛️ Cultural Heritage Explorer

This is my nationwide hackathon-winning project at **HACKQUEST**, called **Cultural Heritage Explorer**. It is a web-based system that detects Indian monuments using a **custom CNN model** and provides informative answers through a **Gradio ChatInterface** powered by the **OpenAI API**. The dataset was entirely self-curated during my internship at **IIT Hyderabad**.

---

## 🔍 Overview

- 🖼️ Image classification of **24 famous Indian monuments** using a customized CNN model.
- 💬 Integration with **OpenAI API** to provide historical and cultural information through a chatbot.
- 🧠 Built using **Flask**, **Gradio**, and chatbot is hosted on **Hugging Face Spaces**.
- 📊 Dataset is custom-built using images collected from the web.

---

## 📁 Dataset

The dataset consists of 24 classes of Indian monuments with images collected manually from Google during the internship.

📌 **Kaggle Dataset Link:**  
[https://www.kaggle.com/datasets/bhaskarjyothula/indian-monuments](https://www.kaggle.com/datasets/bhaskarjyothula/indian-monuments)

### Monument Classes:
- Ajanta Caves  
- Charar-E- Sharif  
- Chhota Imambara  
- Ellora Caves  
- Fatehpur Sikri  
- Gateway of India  
- Hawa Mahal  
- Humayun’s Tomb  
- India Gate  
- Khajuraho  
- Sun Temple Konark  
- Alai Darwaza  
- Alai Minar  
- Basilica of Bom Jesus  
- Charminar  
- Golden Temple  
- Iron Pillar  
- Jamali Kamali Tomb  
- Lotus Temple  
- Mysore Palace  
- Qutub Minar  
- Taj Mahal  
- Tanjavur Temple  
- Victoria Memorial  

---

## 🧠 Model

A customized **Convolutional Neural Network (CNN)** model was trained to classify the 24 monument categories.

📌 **Model Training Notebook:**  
[https://www.kaggle.com/code/bhaskarjyothula/24-monuments](https://www.kaggle.com/code/bhaskarjyothula/24-monuments)

---

## 🌐 Website Features

- 🖼️ Upload an image to detect the monument.
- 💬 Use the ChatInterface to ask questions about monuments.
- 🔗 Powered by OpenAI for generating cultural and historical insights.
- 📦 Combines deep learning model and chatbot in a unified interface.

---

## 🚀 Deployment

The chatbot is deployed on Hugging Face Spaces using **Gradio** and whole website will run using **Flask**.

---

## 🛠️ Tech Stack

- Python  
- TensorFlow / Keras  
- Flask  
- OpenAI API  
- Gradio  
- Hugging Face  
- Kaggle  

---

## 🧩 Integration

- The CNN model predicts the monument from the image.
- The Gradio ChatInterface allows users to ask follow-up questions.
- Flask is used as the backend to serve both the model and chatbot.
- The application brings together **ML predictions + AI-powered responses** in real time.

---

## 👨‍💻 Author

**Jyothula Bhaskar**  
B.Tech in Computer Science & Engineering (AI & ML)  
[LinkedIn](https://www.linkedin.com/in/bhaskar-jyothula-974bbb271/) | [Hugging Face](https://huggingface.co/Bhaskar2611) | [GitHub](https://github.com/Bhaskar2603) | [Kaggle](https://www.kaggle.com/bhaskarjyothula)

---

## 🏁 Acknowledgements

- Special thanks to **IIT Hyderabad** for mentoring me during my internship.
- Kudos to **HACKQUEST** for providing the opportunity to showcase this idea.
- Thanks to **OpenAI**, **Gradio**, **Hugging Face**, and **Kaggle** for their amazing platforms.

---

## 📜 License

This project is intended for educational and research purposes only.  
© 2025 Jyothula Bhaskar
