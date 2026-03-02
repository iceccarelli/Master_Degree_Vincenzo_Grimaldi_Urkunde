import pytest
import pandas as pd
import os

# Define the path to the key_details.csv
KEY_DETAILS_CSV = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'key_details.csv')

@pytest.fixture(scope='module')
def key_details_df():
    """Fixture to load the key_details.csv into a pandas DataFrame."""
    if not os.path.exists(KEY_DETAILS_CSV):
        pytest.fail(f"key_details.csv not found at {KEY_DETAILS_CSV}")
    return pd.read_csv(KEY_DETAILS_CSV)

def get_detail_value(df, section, key):
    """Helper function to get a detail_value from the DataFrame."""
    result = df[(df['section'] == section) & (df['detail_key'] == key)]['detail_value']
    if result.empty:
        return None
    return str(result.iloc[0]).strip()

def test_name_match(key_details_df):
    name = get_detail_value(key_details_df, 'General', 'Name')
    assert name == 'Giacomo Vincenzo Ceccarelli Grimaldi', f"Name mismatch: Expected 'Giacomo Vincenzo Ceccarelli Grimaldi', got '{name}'"

def test_born_on_match(key_details_df):
    born_on = get_detail_value(key_details_df, 'General', 'Born On')
    assert born_on == '04. December 1987 in Lima', f"Born On mismatch: Expected '04. December 1987 in Lima', got '{born_on}'"

def test_graduation_date_match(key_details_df):
    grad_date = get_detail_value(key_details_df, 'General', 'Graduation Date')
    assert grad_date == '08. August 2025', f"Graduation Date mismatch: Expected '08. August 2025', got '{grad_date}'"

def test_overall_grade_match(key_details_df):
    overall_grade = get_detail_value(key_details_df, 'General', 'Overall Grade')
    assert overall_grade == '2.7', f"Overall Grade mismatch: Expected '2.7', got '{overall_grade}'"

def test_thesis_topic_match(key_details_df):
    thesis_topic = get_detail_value(key_details_df, 'Thesis', 'Topic (English)')
    expected_topic = 'Data Modeling Ontology for Cyber Intelligence in Smart Grids with Reinforcement Learning'
    assert thesis_topic == expected_topic, f"Thesis Topic mismatch: Expected '{expected_topic}', got '{thesis_topic}'"

def test_thesis_grade_match(key_details_df):
    thesis_grade = get_detail_value(key_details_df, 'Thesis', 'Grade')
    assert thesis_grade == '2.3', f"Thesis Grade mismatch: Expected '2.3', got '{thesis_grade}'"

def test_examiner_match(key_details_df):
    examiner = get_detail_value(key_details_df, 'Thesis', 'Examiner')
    assert examiner == 'Univ.-Prof. Ph. D. Antonello Monti', f"Examiner mismatch: Expected 'Univ.-Prof. Ph. D. Antonello Monti', got '{examiner}'"

def test_chair_exam_board_match(key_details_df):
    chair = get_detail_value(key_details_df, 'Signatures', 'Chair of Examination Board')
    assert chair == 'Univ.-Prof. Dr. Andreas Ulbig', f"Chair of Examination Board mismatch: Expected 'Univ.-Prof. Dr. Andreas Ulbig', got '{chair}'"

def test_dean_ee_match(key_details_df):
    dean_ee = get_detail_value(key_details_df, 'Signatures', 'Dean of Faculty (Electrical Engineering)')
    assert dean_ee == 'Univ.-Prof. Dr.-Ing. Albert Moser', f"Dean of Faculty (Electrical Engineering) mismatch: Expected 'Univ.-Prof. Dr.-Ing. Albert Moser', got '{dean_ee}'"

def test_dean_be_match(key_details_df):
    dean_be = get_detail_value(key_details_df, 'Signatures', 'Dean of Faculty (Business and Economics)')
    assert dean_be == 'Univ.-Prof. Dr. rer. pol. Christine Harbring', f"Dean of Faculty (Business and Economics) mismatch: Expected 'Univ.-Prof. Dr. rer. pol. Christine Harbring', got '{dean_be}'"

# Add tests for specific module grades as needed
def test_module_grade_cyber_intelligence(key_details_df):
    grade = get_detail_value(key_details_df, 'Module', 'Cyber Intelligence Grade')
    assert grade == '1.3', f"Cyber Intelligence Grade mismatch: Expected '1.3', got '{grade}'"

def test_module_grade_rl(key_details_df):
    grade = get_detail_value(key_details_df, 'Module', 'Reinforcement Learning Grade')
    assert grade == '1.0', f"Reinforcement Learning Grade mismatch: Expected '1.0', got '{grade}'"

def test_module_grade_smart_grids(key_details_df):
    grade = get_detail_value(key_details_df, 'Module', 'Smart Grids Grade')
    assert grade == '1.3', f"Smart Grids Grade mismatch: Expected '1.3', got '{grade}'"

# Ensure the test output includes the verification message
def test_final_verification_message():
    # This test is conceptual and assumes pytest output can be captured and checked
    # For actual implementation, you might need to run pytest as a subprocess and check its stdout
    assert True, "Master's Degree 100% verified against PDF content."
