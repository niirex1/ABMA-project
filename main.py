import os
from bayesian_inference_model import BayesianInferenceModel
from metamorphic_testing import MetamorphicTesting
from dynamic_bayesian_updating import DynamicBayesianUpdating

def load_smart_contract(file_path):
    """
    Load the smart contract source code from the specified file path.
    """
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # Load the smart contract source code
    file_path = input("Enter the path to your smart contract source code: ")
    smart_contract_code = load_smart_contract(file_path)

    # Initialize the Bayesian Inference Model
    bayesian_model = BayesianInferenceModel()
    vulnerability_likelihood = bayesian_model.assess_vulnerabilities(smart_contract_code)
    print(f"Likelihood of vulnerabilities: {vulnerability_likelihood}")

    # Execute Metamorphic Testing
    metamorphic_testing = MetamorphicTesting()
    test_cases = metamorphic_testing.generate_test_cases(smart_contract_code)
    test_results = metamorphic_testing.run_tests(test_cases)

    # Apply Dynamic Bayesian Updating
    dynamic_updating = DynamicBayesianUpdating()
    updated_model = dynamic_updating.update_model(bayesian_model, test_results)
    print("Bayesian model updated based on test outcomes.")

if __name__ == "__main__":
    main()
