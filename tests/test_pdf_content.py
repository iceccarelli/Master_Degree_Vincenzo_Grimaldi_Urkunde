import pytest
import pandas as pd
import os

# Path to the structured metadata (extracted directly from the official RWTH documents)
KEY_DETAILS_CSV = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'key_details.csv')

@pytest.fixture(scope='module')
def key_details_df():
    """Load key_details.csv once for all tests."""
    if not os.path.exists(KEY_DETAILS_CSV):
        pytest.fail(f"key_details.csv not found at {KEY_DETAILS_CSV}")
    return pd.read_csv(KEY_DETAILS_CSV)

def get_detail_value(df, section, key):
    """Helper to safely retrieve a value from the DataFrame."""
    result = df[(df['section'] == section) & (df['detail_key'] == key)]['detail_value']
    if result.empty:
        return None
    return str(result.iloc[0]).strip()

# ====================== GENERAL INFORMATION ======================
def test_full_name_match(key_details_df):
    name = get_detail_value(key_details_df, 'General', 'Full Name')
    assert name == 'Giacomo Vincenzo Ceccarelli Grimaldi', f"Full Name mismatch: got '{name}'"

def test_date_of_birth_match(key_details_df):
    born = get_detail_value(key_details_df, 'General', 'Born On')
    assert born == '04 December 1987 in Lima', f"Born On mismatch: got '{born}'"

def test_graduation_date_match(key_details_df):
    date = get_detail_value(key_details_df, 'General', 'Graduation Date')
    assert date == '08 August 2025', f"Graduation Date mismatch: got '{date}'"

def test_overall_grade_match(key_details_df):
    grade = get_detail_value(key_details_df, 'General', 'Overall Grade')
    assert grade == '2.7', f"Overall Grade mismatch: got '{grade}'"

# ====================== THESIS ======================
def test_thesis_topic_match(key_details_df):
    topic = get_detail_value(key_details_df, 'Thesis', 'Topic (English)')
    expected = 'Data Modeling in a Cross-domain Ontology for Cyber Intelligence in Smart Grids Using Reinforcement Learning'
    assert topic == expected, f"Thesis Topic mismatch: got '{topic}'"

def test_thesis_grade_match(key_details_df):
    grade = get_detail_value(key_details_df, 'Thesis', 'Grade')
    assert grade == '2.3', f"Thesis Grade mismatch: got '{grade}'"

def test_thesis_examiner_match(key_details_df):
    examiner = get_detail_value(key_details_df, 'Thesis', 'Examiner')
    assert examiner == 'Univ.-Prof. Ph. D. Antonello Monti', f"Examiner mismatch: got '{examiner}'"

# ====================== SIGNATURES ======================
def test_chair_of_examination_board_match(key_details_df):
    chair = get_detail_value(key_details_df, 'Signatures', 'Chair of Examination Board')
    assert chair == 'Univ.-Prof. Dr. Andreas Ulbig', f"Chair mismatch: got '{chair}'"

def test_dean_electrical_engineering_match(key_details_df):
    dean = get_detail_value(key_details_df, 'Signatures', 'Dean Faculty Electrical Engineering')
    assert dean == 'Univ.-Prof. Dr.-Ing. Albert Moser', f"Dean (Electrical Engineering) mismatch: got '{dean}'"

def test_dean_business_economics_match(key_details_df):
    dean = get_detail_value(key_details_df, 'Signatures', 'Dean Faculty Business and Economics')
    assert dean == 'Univ.-Prof. Dr. rer. pol. Christine Harbring', f"Dean (Business and Economics) mismatch: got '{dean}'"

# ====================== MODULE GROUPS ======================
def test_engineering_sciences_average_match(key_details_df):
    avg = get_detail_value(key_details_df, 'Module Group', 'Engineering Sciences')
    assert avg == '3.6', f"Engineering Sciences average mismatch: got '{avg}'"

def test_sustainability_corporations_average_match(key_details_df):
    avg = get_detail_value(key_details_df, 'Module Group', 'Sustainability and Corporations')
    assert avg == '2.4', f"Sustainability and Corporations average mismatch: got '{avg}'"
