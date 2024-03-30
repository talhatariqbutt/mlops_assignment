# MLOps Assignment

## Group members:

- i202652 Talha Tariq
- i200951 Hisham Ijaz

### How to Install

1. Clone the repository: `git clone https://github.com/ttsae/mlops_assignment.git`
2. Navigate to the cloned repository: `cd mlops_assignment`
3. Install the requirements: `pip install -r requirements.txt`
4. Train the model: `python train.py`
5. Run the app: `python app.py`
6. Open your browser and go to `http://localhost:5000/`

### Endpoint Usage

- **Endpoint URL**: `http://localhost:5000/predict`
- **Method**: POST
- **Input Data Format**: JSON

Example input data for prediction:

```json
{
  "review": "One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me. The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid. This show pulls no punches with regards to drugs, sex or violence. Its is hardcore, in the classic use of the word."
}
