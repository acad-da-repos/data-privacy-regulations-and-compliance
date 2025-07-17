
import unittest
import pandas as pd
from assignment import anonymize_data

class TestDataPrivacy(unittest.TestCase):
    def test_anonymize_data(self):
        data = {'Name': ['Alice', 'Bob'], 'Email': ['alice@example.com', 'bob@example.com'], 'Age': [25, 30]}
        df = pd.DataFrame(data)
        columns_to_anonymize = ['Name', 'Email']

        anonymized_df = anonymize_data(df.copy(), columns_to_anonymize)

        self.assertEqual(anonymized_df['Name'].iloc[0], '[ANONYMIZED]')
        self.assertEqual(anonymized_df['Email'].iloc[0], '[ANONYMIZED]')
        self.assertEqual(anonymized_df['Age'].iloc[0], 25) # Age should not be anonymized

if __name__ == '__main__':
    unittest.main()
