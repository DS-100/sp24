---
layout: page
title: Graduate Project
nav_order: 3
description: Specifications for the grad project for Data 200.
markdown: kramdown
---
# Graduate Project
{:.no_toc}

<!--### <span style="color:red"> ⚠️ Warning: This webpage is under construction; nothing here is finalized until it is on ds100.org/fa23/gradproject </span>
{:.no_toc} -->

* TOC
{:toc}

## Introduction

The graduate project is **offered only to students enrolled in Data C200, CS C200A, or Data 200S**. Other students are welcome to explore the questions and datasets in the project for personal learning, but their work will not be graded or counted towards their final grades.

The purpose of the project is to give students experience in both open-ended data science analysis and research in general.

<!-- In this project, you will work with **one or any combination** of the following datasets provided to you to explore research questions that you define. -->

<!-- **Project criteria**: In addition to the general guidelines, each dataset option below has its own set of additional requirements for Report Format and Submission. Be sure to consult the correct section for your project option.) 0-->


## Deliverables

The graduate project element will require the following deliverables:

- **Group Formation + Research Proposal:** You will form a project group and submit a google form stating your intended topic and a brief implementation plan. Please see [below](#group-formation--research-proposal) for more information.
- **Checkpoint 1: EDA + Internal Peer Review 1:** Submit a write-up and code for Exploratory Data Analysis on your dataset. Additionally, submit an internal peer review. More information [below](#checkpoint-1-eda--internal-peer-review).
- **Checkpoint 2: Mandatory Check-In:** Write a one-pager of your progress, focusing on the modeling approaches your team explored, and review it with a course staff member. Further details [below](#checkpoint-2-mandatory-check-in).
- **Internal Peer Review 2:** Submit the second internal peer review form.
- **Project Report First Draft:** Submit the first draft of your report, detailing your EDA and modeling efforts, along with any necessary code.
- **External Peer-Review:** Provide feedback on other teams' work.
- **Final Project Report:** Submit the final project report, including all necessary code. Ensure all relevant feedback from the first draft and external peer reviews are incorporated. Additionally, you are required to submit your test set results and make a brief 5-minute YouTube video recording of the project.


### Teamwork

**You must work in groups of two or three students.** In order to give everyone experience in collaborating on a data science project, individual projects are not allowed. Everyone in the same group will receive the same grade (except for exceptional circumstances).

## Timeline and Grading Breakdown

<!-- [Internal Peer Review](https://forms.gle/cied6ZzmBToj3ARP9) -->

| Deadline (at 11:59 PM Pacific) | Event / Deliverable                        | Link                                                           | Grading Weight |
|--------------------------------|--------------------------------------------|----------------------------------------------------------------|----------------|
| 3/15                           | [Research Proposal and Project Groups]((https://www.gradescope.com/courses/696886/assignments/4322203){:target="_blank"})   | [Proposal Form](https://forms.gle/DcBp3ZbM8TpTfSRD6){:target="_blank"}             | 5%             |
| 3/22 ([3/24 Extension](https://edstem.org/us/courses/51810/discussion/4604306){:target="_blank"})                           | [Checkpoint 1: EDA]((https://www.gradescope.com/courses/696886/assignments/4247160){:target="_blank"}) + [Internal Peer Review 1](https://www.gradescope.com/courses/696886/assignments/4327698){:target="_blank"} |  [Internal Peer Review Form](https://forms.gle/NgERYS9bd1U29Xur5){:target="_blank"}   | 10%            |
| Week of 4/8                    | [Checkpoint 2: Mandatory Check-in with TA]((https://www.gradescope.com/courses/696886/assignments/4312054){:target="_blank"})   |                                                                | 7.5%           |
| 4/19                           | Internal Peer Review 2 Due                 |   [Internal Peer Review Form](https://forms.gle/XpYfvoMrNHBq8cFy7){:target="_blank"}                                                             | 5%            |
| 4/26                           | First Draft of Final Report Due            |                                                                | 15%           |
| 5/3                            | External Peer Review Due                   |                                                                | 7.5%           |
| 5/10                           | Final Project Report and Presentation Video|                                                                | 50%            |

### Late Policy
- **No Extensions for First Draft**: The first draft cannot be submitted late as it is crucial for the peer review process.
- **Final Report and Presentation Video**: Late submissions incur a 10% daily penalty, up to a maximum of two days. Submissions are rounded to the nearest day (e.g., 2 minutes late counts as 1 day late).
- **Peer Reviews and Other Deliverables**: Must be submitted on time; no extensions are permitted.

## Datasets

Please choose one of the following datasets to work on. **You will be expected to complete all (2) tasks provided for your chosen dataset.**
<!-- In general, if you're drawing any conclusions regarding causality, please be sure to consult the [extra resources on causal inference](#extra-resources-causal-inference). -->

### Accessing Datasets

All of the provided datasets can be found in the Datahub directory `shared/sp24_grad_project_data`. You can access the data directly from Datahub. If you wish to work on the project locally, you can also download the files containing the datasets for each topic by right-click on the file in JupyterLab and select "Copy Download Link". If you choose to train more complex models, DataHub might not have enough hardware resources or memory, in which case you can use [Google Colab](https://colab.google/){:target="_blank"} or your local machine. If you would like to use Google Colab, feel free to check out this [link](https://stackoverflow.com/questions/48376580/how-to-read-data-in-google-colab-from-my-google-drive){:target="_blank"} to get started.

### Topic 1: Computer Vision
In disaster situations, it is important for emergency response efforts to have access to quick and accurate information about an area in order to respond effectively. This project will explore how data science techniques can be useful for such efforts.

#### Project Goals
{:.no_toc}
- Learn to work with image data by learning to use common feature extraction techniques like Sobel edge filtering.
- Learn to work on real-world data with common complexities such as class imbalance, low signal-to-noise ratio, and high dimensional data.
- Learn how to design effective preprocessing and featurization pipelines for solving difficult machine learning tasks.

#### Mission
{:.no_toc}
You have been hired by a crisis response agency to help assist them with your impressive data science skills! The agency has found that using satellite imagery is highly useful for supplying information for their response efforts. Unfortunately, however, annotating these high-resolution images can be a slow process for analysts. Your mission is to help address this challenge by developing an automatic computer vision approach!

#### Dataset Description
{:.no_toc}
The agency would like you to develop your approach on their internal dataset, derived from the [xView2 Challenge Dataset](https://xview2.org/){:target="_blank"}. This dataset contains satellite images of buildings after various natural disasters. The buildings are labeled based on the level of damage sustained on a scale ranging from 0 (no damage) to 3 (destroyed).

You can access all of the data within the `./satellite-image-data` directory. The dataset consists of the following folders for different natural disasters
1. `midwest-flooding`
2. `socal-fire`
3. `hurricane-matthew`

Within each folder is a zip file `train_images.npz` containing the satellite images as numpy arrays and a `train_labels.npy` file with corresponding damage level labels.

> Testing: In the main directory, there are also the `test_images_hurricane-matthew.npz` and `test_images_flooding-fire.npz` zip files. The first contains test images from the `hurricane-matthew` disaster and the latter consists of a combination of test images from `midwest-flooding` and `socal-fire`.

#### Getting Started
{:.no_toc}
To help you with onboarding, the agency has provided a starter notebook [`starter.ipynb`](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsp24-student&urlpath=lab%2Ftree%2Fsp24-student%2Fgrad-proj%2Fcv-satellite-images%2Fstarter.ipynb&branch=main){:target="_blank"} which will introduce you to the dataset and some useful internal tools. After completing the onboarding assignment you will be comfortable with the following:
1. Loading and visualizing data using tools from `data_utils.py`
2. Processing different color channels in the dataset images.
3. Extracting feature information from images using tools from `feature_utils.py`.

#### Exploratory Data Analysis
{:.no_toc}
Now that you have successfully been onboarded, the agency would like you to start performing some exploratory data analysis to build an initial understanding of the data. As part of the exploratory data analysis, the agency is interested in understanding certain aspects of the dataset better. Specifically, they are looking for:

- Basic statistics about the dataset, such as the number of images per disaster type and the distribution of image sizes and damage labels.
- Insights into useful image features for classifying images based on disaster type or damage level. Previous interns have found color information to be potentially useful. You are tasked with verifying this and exploring whether color features can effectively differentiate:
    - `midwest-flooding` from `socal-fire` images.
    - Damage levels 1 and 3 within the `hurricane-matthew` dataset.

Please prepare an EDA report to present to the agency leadership with the above in mind.

#### Project Tasks
{:.no_toc}
Now that leadership is pleased with your initial EDA report and confident in your data science ability, they would like you to assist the agency with various tasks. *Please complete Task A first and then Task B.*

#### *Task A: Disaster Type Classification*
{:.no_toc}
The agency consists of different subdivisions for assisting with different disaster types, e.g., fires, floods, etc. In the event of a disaster, the agency mounts its response effort by first assessing the type of disaster and then requesting the appropriate subdivision to assist with the disaster.

Your task is to assist the agency with making this initial call quickly by automatically classifying images based on the disaster scenario. Specifically, your role will be to build a classifier that can distinguish images from the `midwest-flooding` disaster and the `socal-fire` disaster.

To assess your performance, please submit predictions for the `test_images_flooding-fire.npz` images. This should be in a csv file `test_images_flooding-fire_predictions.csv` consisting of a single column with no header, with a 0 to indicate a `midwest-flooding` prediction and a 1 to indicate a `socal-fire` prediction. The prediction in row *i* should correspond to the *ith* image.

#### *Task B: Damage Level Classification*
{:.no_toc}
The agency needs to know how severe a disaster is in order to allocate resources for a response effectively. The agency is especially concerned with human lives and uses building damage as an important metric for disaster severity.

Your task is to assist the agency by automatically detecting the building damage level after a disaster. Specifically, create a damage level classifier for the `hurricane-matthew` disaster.

To assess your performance, please submit predictions for the `test_images_hurricane-matthew.npz` images. This should be in a CSV file `test_images_hurricane-matthew_predictions.csv` consisting of a single column with no header, with a 0-3 prediction of the damage level. The prediction in row *i* should correspond to the *i*th image.

#### Resources
{:.no_toc}
To assist you in your efforts the agency has compiled the following list of resources:
- For more background about the dataset you can look at the [paper](https://arxiv.org/pdf/1911.09296.pdf){:target="_blank"} associated with the dataset.
- For image processing, [scikit-image](https://scikit-image.org/){:target="_blank"} is a very useful library. This [tutorial](https://www.kaggle.com/code/bextuychiev/full-tutorial-on-image-processing-in-skimage){:target="_blank"} may be helpful for learning how to use the library.
- For problems with imbalanced classes, the [imblearn](https://imbalanced-learn.org/stable/index.html){:target="_blank"} library has useful tools and examples.


### Topic 2: Natural Language Processing

A common task in real-life data analysis involves working with text data.
In this project, we will work with a dataset consisting of natural language questions asked by humans and answers provided by chatbots.

#### Project Goals
{:.no_toc}
- Prepare you to work with text data by learning common techniques like embedding generation, tokenization, and topic modeling.
- Work with real-world data in its targetted domain. The data is non-trivial in both size and complexity.
- Ask open-ended questions and answer them using data at hand.

#### Dataset Description
{:.no_toc}
The source dataset link is [here](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations){:target="_blank"}. The author describes the dataset as follows:

> This dataset contains 33K cleaned conversations with pairwise human preferences. It is collected from 13K unique IP addresses on the Chatbot Arena from April to June 2023. Each sample includes a question ID, two model names, their full conversation text in OpenAI API JSON format, the user vote, the anonymized user ID, the detected language tag, the OpenAI moderation API tag, the additional toxic tag, and the timestamp.

[Chatbot Arena](https://chat.lmsys.org/){:target="_blank"} is a platform where users can ask questions and two chatbots will provide answers. The user then votes on which chatbot provided the best answer. The dataset contains the questions, the answers, and the user votes.

You can find the processed dataset in `./chatbot-arena-conversations.jsonl.gz`. The dataset is in JSON line format and compressed using gzip. It has gone through the following preprocessing steps to make analysis easier:

- Removed non-English conversations.
- Removed conversations with more than one round.
- Removed conversations classified as toxic or harmful.

The dataset you will be working with contains `25322` rows (out of `33000` total rows) and `7` columns ([example row](https://gist.github.com/simon-mo/25c5d532bccc7f28b404cffdfe719e6e#file-example-row-json){:target="_blank"}). The columns are:

- `question_id`: A unique identifier for the question.
- `model_a`: The name of the first chatbot model.
- `model_b`: The name of the second chatbot model.
- `winner`: The name of the chatbot model that won the user vote.
- `judge`: The anonymized user ID that voted.
- `conversation_a`: The conversation between the user and `model_a`.
- `conversation_b`: The conversation between the user and `model_b`.

There are two auxiliary datasets that you can use to help with your analysis:

- `./chatbot-arena-prompts-embeddings.npy` contains the 256-dimensional text embeddings for each of the human questions. The embeddings are generated using OpenAI's `text-embedding` model. We will explain what embeddings are and how you can use them later.
- `./chatbot-arena-gpt3-scores.jsonl.gz` ([example row](https://gist.github.com/simon-mo/25c5d532bccc7f28b404cffdfe719e6e#file-example-aux-row-json){:target="_blank"}) contains labels for the dataset you can use for later modeling tasks. It has the following fields:
  - `question_id`: The unique identifier for the question, as seen in `./chatbot-arena-conversations.jsonl.gz`.
  - `prompt`: The extracted human question. This is equivalent to the first message in `conversation_a` and `conversation_b` in `./chatbot-arena-conversations.jsonl.gz`.
  - `openai_scores_raw_choices_nested`: The response from OpenAI GPT 3.5 model (see later for the prompt). It contains the evaluated topic model, the reason for a hardness score from 1 to 10, and the value. For each prompt, we have 3 responses from GPT 3.5 because it is a probablistic model. In fact, you will find in real world there are common multiple labels from different annotators for ground truth data. We extracted the fields into the columns below.
  - `topic_modeling_1`, `topic_modeling_2`, `topic_modeling_3`: The topic modeling for the first, second, and third response. Each topic should have two words.
  - `score_reason_1`, `score_reason_2`, `score_reason_3`: The reason for the hardness score for the first, second, and third response.
  - `score_value_1`, `score_value_2`, `score_value_3`: The hardness score for the first, second, and third response.

We used [this prompt](https://gist.github.com/simon-mo/25c5d532bccc7f28b404cffdfe719e6e#file-prompt-md){:target="_blank"} to generate the responses. You are welcome to generate your own ground truth data. You can generate your own embeddings following [this](https://gist.github.com/simon-mo/25c5d532bccc7f28b404cffdfe719e6e#file-using-your-own-embeddings-md){:target="_blank"} guide.

#### Exploratory Data Analysis
{:.no_toc}
For the EDA tasks, tell us more about the data. What do you see in the data? Come up with questions and answers about them. For example, what is the win rate of GPT4?  What are the most common topics? Do different judges have different preferences? What are the most common topics? What are the most common reasons for a question being hard?

#### Project Tasks
{:.no_toc}
Now, we aim to better understand the different chatbot models! Please complete both Task A and B. We have included example questions to consider, but you are expected to come up with your own questions to answer.

For both tasks, you will be working with the data provided. But you are also expected to perform prediction on a holdout set. You can find the data in `arena-validation-set-prompt-only.jsonl.gz` in the same directory. The data contains fields `question_id`, `prompt`, `model_a`, and `model_b`. You are expected to predict the winner and the hardness score for tasks A and B respectively. You should submit your final prediction as a `csv` file with three columns `question_id`, `winner`, `hardness_score`. The `winner` column should be one of the four values: `model_a`, `model_b`, `tie`, or `tie (bothbad)`. The `hardness_score` should be an integer from 1 to 10.

#### *Task A: Modeling the Winning Model*
{:.no_toc}
Given a prompt, can we predict which model's response will win the user vote? You can start by analyzing the length, textual features, and embeddings of the prompt. You should also explore the difference in output of the different models. For modeling, you can use logistic regression or other modeling techniques to perform classification to predict the winner for the holdout set given `prompt`, `model_a`, and `model_b`. You should also evaluate the model using appropriate metrics.

One hint would be to utilize topic modeling data by first clustering prompts given their embeddings, then for each cluster, train a model to predict the winner. Also, feel free to use the hardness score to help with the prediction.

#### *Task B: Hardness Prediction*
{:.no_toc}
While we provide the hardness score generated by GPT3.5, can you explore whether such scoring is useful and valid? For hardness score, we want it to be an integer value from 1 to 10. For example, if a prompt's score is 1, we expect the weak model to be able to answer the question. If the score is 10, we expect the question to be hard, maybe only GPT4 can answer it.

You can start by analyzing the embeddings and the topic modeling data. You can then use linear regression to predict the hardness score, using existing or new features.

You should also evaluate the model using appropriate metrics. One challenging aspect here is that the output score should be integer value, while linear regression is used for continuous data.

#### Getting Started
{:.no_toc}
To get started, we provide a notebook [`nlp-chatbot-starter.ipynb`](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsp24-student&urlpath=lab%2Ftree%2Fsp24-student%2Fgrad-proj%2Fnlp-chatbot-arena%2Fnlp-chatbot-starter.ipynb&branch=main){:target="_blank"} that demonstrates how to load and inspect the data.

Additionally, here are some example questions about the project that you are welcome to explore.

> Modeling: Perform some modeling tasks given our ground truth labels. Can you train a logistic regression model to predict the winner given embeddings? How about a K-means clustering model to cluster the questions? Can you use linear regression to predict the hardness score? We expect you to demonstrate how the well model works and how to evaluate them. You should justify the choice of model and the evaluation metrics. You should also discuss the limitations of the model and how to improve them.

> Analysis: By leveraging the question embeddings, can we find similar questions? How repeated are the questions in the dataset? Can you reproduce the Elo score rating for the chatbots and come up with a better ranking? How can we make sense of the data overall?

#### Resources
{:.no_toc}
- [Joey's EDA and Elo rating modeling](https://colab.research.google.com/drive/1KdwokPjirkTmpO_P1WByFNFiqxWQquwH){:target="_blank"} is a great resource to get started with the EDA. Note that (1) the plot is made with Plotly, we recommend you to reproduce the plot with Matplotlib or Seaborn, and (2) the Elo rating is a good modeling task to reproduce but we expect you to do more than just that (for example, demonstrate how Elo rating works and how to calculate it in your report).

- [An intuitive introduction to text embeddings](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/){:target="_blank"} is a good resource to understand what is text embeddings and how to use them.

- [Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system){:target="_blank"} and [Bradley-Terry model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model){:target="_blank"} are essential to model a ranking among the pairwise comparison.

- [Huggingface pipeline](https://huggingface.co/docs/transformers/en/main_classes/pipelines){:target="_blank"} has many implementations of common NLP tasks for you to use, including sentiment analysis, summarization, text classification, etc.

- [spaCy](https://spacy.io/usage/spacy-101){:target="_blank"} is a wonderful library containing classifical NLP tasks like tokenization, lemmatization, etc.

## Group Formation + Research Proposal

The first deliverable of your group project is just to form your group, choose a dataset, and submit your implementation plan to [this google form](https://forms.gle/DcBp3ZbM8TpTfSRD6){:target="_blank"} by 11:59 pm on 3/15. The implementation plan should consist of a series of steps for completing the project along with a timeline. You may form groups of 2 or 3 people with any Data 200/200A/200S student.

## Checkpoint 1: EDA + Internal Peer Review

The checkpoint is intended to keep you on track to meet your project goals. You will need to submit an exploratory data analysis report to Gradescope. This will include submitting both a report of your results so far as well as all code necessary to replicate your results. Please answer all the questions below. Your submission should include:

<!-- - **Project Introduction and Goals:** Please briefly introduce your project. Think about introducing your project to someone who has a background in data science but does not know the dataset and your research question. This part should not exceed 500 words. Here are some components to help you get started:
  - What is the dataset about? How was the data collected? What are the available features and information? What is the size of the dataset?
  - What questions do you plan to ask about the dataset? Why do we care about such a problem?
  - What is your workflow for the project? Your first step, second step…
  - What are the models you plan to use? Why would the model be a good fit for your project? What are potential pitfalls you could run into?
  - What is your goal for the project? What are the expected deliverables? -->

- **Data Sampling and Collection**
  - How was the data read and sampled for your EDA process?
  - Was there any potential bias introduced in the sampling process?
- **Data Cleaning**
  - What type of data are you currently exploring?
  - What is the granularity of the data?
  - What does the distribution of the data look like? Are there any outliers? Are there any missing or invalid entries?
  - The data is not structured. How did you turn it into a structured format? What features have you engineered?
- **Exploratory Data Analysis**
  - Is there any correlation between the variables you are interested in exploring?
  - How would you cleanly and accurately visualize the relationship among variables?
  - What are your EDA questions? (For example, are there any relationships between A and B? What is the distribution of A?).
  - Do you need to perform data transformations?
- **Figures(tables, plots, etc.)**
  - Descriptions of your figures. Takeaways from the figures.
  - These figures must be of good quality (i.e. they must include axes, titles, labels, etc.) and they must be relevant to your proposed analysis.

Concretely, here are the minimal requirements for EDA for each project. Using your knowledge from Data 200, what would be appropriate data visualizations? You are welcome to do more than the minimal requirements.
- **Computer Vision**:
  - Number of images per disaster.
  - Image sizes in each dataset. Should ideally observe large variance in sizes, but similar distribution for each disaster.
  - Damage labels. Should observe imbalances in the labels.
  - (Open-ended) Visualize the distribution of color for different disasters.
  - (Open-ended) Convey that the distributions are “separable” somehow.
- **Natural Language Processing**:
  - Ranking of the model based on their win rate or ELO ratings.
  - Distribution of the prompt and response length.
  - Hardness score distribution and its correlation with the models (e.g. GPT4 wins on hardest prompts).
  - (Open-ended) Visualize the "variance" in model performance (see [LMSys Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard) for an example).
  - (Open-ended) Explore the prompt topics in the dataset (topic modeling).

Every member of the group also needs to submit the internal peer review [form](https://forms.gle/NgERYS9bd1U29Xur5){:target="_blank"} for this checkpoint. This form is intended to record your and your group members' progress in the project. The records will be confidential to the teaching staff and will not be shared with other students.

<!-- - **Other Preliminary Results (optional)**: Please optionally post any other preliminary results here for our information. -->

## Checkpoint 2: Mandatory Check-In

The purpose of this checkpoint is to ensure you are making progress and on schedule to submit the first draft of the project in approximately two weeks time. You will be required to make a document summarizing all of your progress so far, including your EDA and modeling results. You will be required to submit the report to Gradescope before the meeting. The staff member will skim the report before the meeting and give you guidance on the project as a whole.

For the check-in we would like for you to prepare brief answers to the following questions about the modeling process:
- What model do you plan on using and why?
- Does your model require hyperparameter tuning? If so, how do you approach it?
- How do you engineer the features for your model? What are the rationales behind selecting these features?
- How do you perform cross validation on your model?
- What loss metrics are you using to evaluate your model?
- From a bias-variance tradeoff standpoint, how do you assess the performance of your model? How do you check if it is overfitting?
- How would you improve your model based on the outcome?
- Are there any further extensions to your model that would be worth exploring?

## Checkpoint 3: Project Report First Draft + Internal Peer Review

The first draft of your final report, please see below for more information on what you should aim to submit. You do not need to submit the video and test set performance components for checkpoint 3, but you are expected to submit a comprehensive written report that summarizes your analysis.

## Final Project Report
The project submission should include the following four components:

### [Component 1] Analysis Notebooks (10%)

This component includes all the Jupyter Notebook(s) containing all the analyses that you performed on the datasets to support your claims in your write-up. Make sure that all references to datasets are done as `data/[path to data files]`. By running these notebooks, we should be able to replicate all the analysis/figures done in your write-up.

Your analysis notebook(s) should address all of the following components in the data science lifecycle. Please note that a thorough explanation of your thought process and approach is **as important as** your work. Unreadable/uncommented code will lose points. Along with the code for the EDA portion (which also has to be included), we have provided a few additional preliminary questions/tips you can consider for the modeling portion of the project:

  - Which model(s) do you use and why?
  - How do you use your data for training and testing?
  - Does your model require hyperparameter tuning? If so, how do you approach it?
  - How do you engineer the features for your model? What are the rationales behind selecting these features?
  - How do you perform cross-validation on your model?
  - What loss metrics are you using to evaluate your model? Why?
  - From a bias-variance tradeoff standpoint, how do you assess the performance of your model? How do you check if it is overfitting?
  - How would you improve your model based on the outcome?
  - Are there any further extensions to your model that would be worth exploring?


### [Component 2] Project Write-Up (20%)

This is a single PDF that summarizes your workflow and what you have learned. It should be structured as a research paper and include a title, list of authors, abstract, introduction, description of data, methodology, summary of results, discussion, conclusion, and references. Make sure to number figures and tables, include informative captions, and ensure you include the provenance of the figures in the main narrative. We encourage you to render the PDF using LaTeX, but we will not be able to provide assistance with LaTeX-related issues.

Specifically, you should ensure you address the following in the narrative:

<!-- * Clearly state the research questions and why they are interesting and important. -->
* Introduction: ensure you include a brief survey of related work on the topic(s) of your analysis. Be sure to reference current approaches/research in the context of your project, as well as how your project differs from or complements existing research. You must cite all the references you discuss in this section.
* Description of data: ensure you outline the summary of the data and how the data was prepared for the modeling phase (summarizing your EDA work). If applicable, descriptions of additional datasets that you gathered to support your analysis may also be included.
* Methodology: carefully describe the methods/models you use and why they are appropriate for answering your research questions. You must include a detailed description of how modeling is done in your project, including inference or prediction methods used, feature engineering and regularization if applicable, and cross-validation or test data as appropriate for model selection and evaluation. You may also include interesting findings involving your datasets.
* Summary of results: analyze your findings in relation to your research question(s). Include/reference visualizations and specific results. Discuss any interesting findings from your analysis. You are encouraged to compare the results using different inference or prediction methods (e.g. linear regression, logistic regression, or classification and regression trees). Can you explain why some methods performed better than others?
* Discussion: evaluate your approach and discuss any limitations of the methods you used. Also, briefly describe any surprising discoveries and whether there are any interesting extensions to your analysis.

The narrative PDF should include figures sparingly to support specific claims. It can include a few runnable code components, but it should not have large amounts of code. The length of the report should be 8 ± 2 pages when it is printed as a PDF, excluding figures and code.

Tip: if you need to write a large amount of LaTeX on markdown, you may want to use the `%%latex` cell magic. However, we also encourage you to explore [Overleaf](https://www.overleaf.com) for easily writing clean LaTeX documents.

Please submit everything as a zip file to the final report submission portal on Gradescope. Please make sure the folder in the zip file has the following structure:

```
[your studentIDs joined by _]/
    data/[all datasets used]
    analysis/[analysis notebooks]
    narrative/[narrative PDF]
    figures/[figures included in the narrative PDF]
```

Please use student IDs joined by `_` as the name for the top-level directory. The analysis notebooks must be runnable within this directory structure. If the narrative PDF includes any figures that are created in the analysis notebooks, the figures should be saved to `figures/` by the analysis notebooks.

### [Component 3] Test Set Performance (10%)

This component of the final report will be graded based on your models' performance on the test set for both tasks of your chosen project (please find the thresholds for each task in the rubrics). You will need to submit your predictions to Gradescope to get your test performance; you will be allowed to upload up to 4 times a day. Please find the test data for each task for both projects below. 

#### **Topic 1 (CV)**

`test_images_flooding-fire.npz` is the test for Task A and `test_images_hurricane-matthew.npz` is the test set for Task B; both files are located in `shared/sp24_grad_project_data/satellite-image-data` directory on Data 100 Datahub.

Please submit two CSV files named `test_images_flooding-fire_predictions.csv`, and `test_images_hurricane-matthew_predictions.csv` to [this](https://www.gradescope.com/courses/696886/assignments/4365006){:target="_blank"} Gradescope assignment. Each CSV should only contain one column named `pred`.

#### **Topic 2 (NLP)**

Here are the test sets for both tasks - `arena-validation-set-prompt-only.jsonl.gz`, `arena-validation-set-prompts-embeddings.npy`, and `arena-validation-set-topic-modeling.jsonl.gz`; all files are located in `shared/sp24_grad_project_data/nlp-arena-data` directory on Data 100 Datahub.

Submit a single CSV file with three columns named `question_id`, `winner`, `hardness_score` to [this](https://www.gradescope.com/courses/696886/assignments/4364990){:target="_blank"} Gradescope assignment.

### [Component 4] Video Recording (10%)

Details will be released soon.


## Rubrics
This section includes a rubric for how different project deliverables are going to be graded. This section will be updated as we get further along the project timeline.

### Group formation + Research Proposal (5%)
- Short paragraph description of implementation plan and timeline (2%).
- Forming teams by the deadline (3%).

### Checkpoint 1: EDA + Internal Peer Review (10%)
- Data Sampling and Collection (0.5%).
- Data Cleaning (3%).
- Exploratory Data Analysis (3%).
- Figures (tables, plots, etc.) (3%).
- Internal Peer Review (0.5%).

### Checkpoint 2: Mandatory Check-In (7.5%)
- Exploratory Data Analysis (1.5%).
- Feature Engineering (2%).
- Modelling Approaches (3%).
- Preliminary Results (1%).

### Checkpoint 3: Project Report First Draft + Internal Peer Review (20%)
Please refer to the section on the [Final Project Report](#final-project-report) for more information on how your first draft will roughly be graded. Your first draft will be graded more leniently than your final submission, but we’re still looking for largely the same elements. You do not need to submit the video and test set performance components for checkpoint 3, but you are expected to submit a comprehensive written report that summarizes your analysis.

The internal peer review is a simple google form checking if each member of the group is contributing to the project and how the tasks are distributed among members. This is graded on completion.

### External Peer Review (7.5%)

Each student will peer review a project from another group; each student will be graded separately based on the feedback they provide in their review. The review will be graded by staff out of a total of 5 points. Each review should include the following components:

1. (1.5%) A summary of the report. The summary should address at least the following:
  - What is the conclusion drawn from the EDA and modeling results?
  - What data modeling/inference techniques do the group primarily use to gain insights into their research question? Why are these techniques suitable for the task?
  - What are the next steps a researcher can take if they want to improve their model further based off the work in the project?

2. (6%, 1% per component) An evaluation of the report based on the Data Science Lifecycle. The review should include at least **one strong point and one suggestion for improvement** for each of the following components in the project:
  - Data collection and sampling
  - Data cleaning
  - Exploratory data analysis (data wrangling, visualization, etc.)
  - Data modeling (feature engineering, selection of the model, and evaluation of the model's performance, etc.)
  - Inference (do the results from the model sufficiently support the conclusion within the report?)
  - Discussion (does the report effectively discuss the limitations of the methods used and the implications of the results?)

The external peer review is also a great chance to learn from other people's work and reflect on the work of your own.

### Final Project Report (50%)
* Analysis Notebooks (10%)
* Project Writeup (20%)
* Modeling Performance (10%)
* Presentation Video (10%)

### Final Report: Analysis Notebook

| Criterion                                             | Points|
|-------------------------------------------------------|-------|
| Code readability and documentation                    | 3     |
| Proper and sufficient utilization of Python libraries | 2     |
| Overall code quality                                  | 2     |
| Replicability of the results                          | 3     |
| **Total**                                             | **10**|

### Final Report: Project Writeup

| Criterion                                                              | Points|
|------------------------------------------------------------------------|-------|
| Exploratory data analysis                                              | 3     |
| Modeling and inference techniques                                      | 6     |
| Analysis of results                                                    | 5     |
| Implementation of peer review feedback                                 | 2     |
| Discussion of potential societal impacts and/or ethical concerns       | 2     |
| Overall clarity and structure of the report                            | 2     |
| **Total**                                                              | **20**|

### Final Report: Modeling Performance

#### **Topic 1 (CV)**

| Task (metric) | Threshold | Points |
|---------------|-----------|--------|
| Task A (accuracy) | 0.8131  |   3    |
|               | 0.9003  |   4    |
|               | 0.9927  |   5    |
| Task B (F1 score)  | 0.3987  |   3    |
|               | 0.4334  |   4    |
|               | 0.5602  |   5    |

#### **Topic 2 (NLP)**

| Task (metric)     | Threshold | Points |
|-------------------|-----------|--------|
| Task A (accuracy) | 0.50      |   3    |
|                   | 0.54      |   5    |
| Task B (MSE)      | 2.78      |   3    |
|                   | 2.5       |   5    |



<!-- ## Extra Resources: Causal Inference

When studying the relationship between datasets, you might want to consult the following references on causality vs. correlation. Oftentimes, it is tempting to make claims about causal relationships when there is not enough evidence from the data to support such claims. Please review the following references, or other reputable references that you find on the topic to familiarize yourself with relevant concepts and methods.

* [Data 102  Data, Inference, and Decisions Spring 2020: Lecture 13: Causal Inference I. Moritz Hardt.](https://data102.org/sp20/assets/notes/notes13.pdf)
* [Hernán MA, Robins JM (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC.](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* [Advanced Data Analysis from an Elementary Point of View by Cosma Rohilla Shalizi](https://www.stat.cmu.edu/~cshalizi/ADAfaEPoV/) -->
