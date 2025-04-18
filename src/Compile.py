from solcx import compile_standard, install_solc
import json


def Compile_Solidity(contract_file):
    install_solc("0.8.13")
    with open(contract_file, "r") as file:
        source_code = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {contract_file: {"content": source_code}},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "evm.bytecode"]
                    }
                }
            },
        },
        solc_version="0.8.13",
    )

    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

    return compiled_sol

if __name__ == "__main__":  
    compiled_sol = Compile_Solidity("./src/newContract.sol")
    with open('./Compiled/newContract.json', 'w') as file:
        json.dump(compiled_sol, file)
    
    print(" Contract compiled successfully and saved to Compiled/newContract.json")

