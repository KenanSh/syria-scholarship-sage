# Syria-Scholarship-Sage
This project focuses on developing an **Arabic** AI Assistant integrated into a website, specifically designed for accessing information about Scholarships and Internships worldwide. It is worth noting that the initial version of the assistant was in English.

The primary objective of this assistant is to assist visitors in navigating the website to discover relevant Scholarships or Internships. Additionally, it aids students by addressing questions related to their academic life.

The implementation utilizes the **Rasa Framework**, a leading open-source conversational AI platform that emphasizes Natural Language Understanding (NLU).

## Dataset

### Manually Gathered Dataset

For the navigation task, the NLU is trained on nine general-purpose Arabic sentences collected from four different individuals. For the **Academic Assisting** aspect, data was gathered through a questionnaire distributed to university students. The collected data was then analyzed to identify 14 distinct academic problems faced by students. Responses to these problems were sourced from academic assistants across various faculties and integrated into the chatbot's domain file.

## Why Rasa Framework?

1. Open-Source Framework.
2. Suitable for interactive assistance, providing a more dynamic experience compared to static question-answering or expert systems.
3. Rasa's robust NLU capabilities enable effective training with minimal examples, ensuring accurate user input recognition in the desired dialect.
4. Integration capabilities with various external systems and APIs.
5. Customizability to tailor the chatbot's behavior according to the unique requirements of the application.

Some Testing Scenarios:

1. ![image](https://github.com/KenanSh/syria-scholarship-sage/assets/101220492/80fb0499-3aea-4075-ad20-4f148b92e2c2)
2. ![image](https://github.com/KenanSh/syria-scholarship-sage/assets/101220492/3945ea69-6bbc-4cb8-8c57-98e39d8bf4ee)

**Note: First version was in English**
