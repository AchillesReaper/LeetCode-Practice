To use nvm (Node Version Manager) for a LeetCode project, you aren't just creating a folder; you're setting up a specialized environment where you can write and execute TypeScript without a heavy build step.

Here is the step-by-step workflow to get your LeetCode playground up and running.

1. Set the Node Version with NVM<br/>
    First, ensure you are using a modern version of Node. LTS (Long Term Support) is usually the safest bet for stability.<br/>

    ``` Bash 
    # Install and use the latest LTS version
    nvm install --lts
    nvm use --lts
    ```

2. Initialize the Project Folder<br/>
    
    ``` Bash
    mkdir leetcode-practice
    cd leetcode-practice
    npm init -y
    ```

3. Install TypeScript and ts-node<br>
    You’ll need typescript for type checking and ts-node to run .ts files directly in your terminal without manual compilation.

    ``` Bash
    # Install dependencies as 'devDependencies' (-D)
    npm install -D typescript ts-node @types/node
    ```

4. Configure TypeScript<br>
    Generate a `tsconfig.json` file. This tells TypeScript how to treat your code.

    ``` Bash
    npx tsc --init
    ```
    Tip: In your `tsconfig.json`, ensure `"target": "ESNext"` and `"module": "CommonJS"` are set so `ts-node` plays nicely with your imports/exports.

5. Structure Your Solutions<br>
    I recommend organizing by problem number or name. Here is a clean structure:

    ``` Plaintext
    leetcode-practice/
    ├── node_modules/
    ├── package.json
    ├── tsconfig.json
    ├── solutions/
    │   ├── 001-two-sum.ts
    │   └── 020-valid-parentheses.ts
    └── utils/
        └── linked-list-helper.ts (optional helpers)
    ```

6. How to Run Your Code<br>
    Since you've installed ts-node locally (which is best practice), you run it using `npx`.

    Example Solution (`solutions/001-two-sum.ts`):

    ``` TypeScript
    function twoSum(nums: number[], target: number): number[] {
        console.log("Solving Two Sum...");
        return [0, 1]; // Placeholder
    };

    console.log(twoSum([2, 7, 11, 15], 9));
    ```

    Run it in the terminal:

    ``` Bash
    npx ts-node solutions/001-two-sum.ts
    ```

Pro-Tip: The `.nvmrc` File
To make this truly an "nvm project," create a file named `.nvmrc` in your root folder:

    ``` Bash
    node -v > .nvmrc
    ```
Now, whenever you or anyone else enters this folder, they can simply type `nvm use` and it will automatically switch to the exact Node version you used for these solutions.


put it simple
```Bash
    nvm use
    npx ts-node solutions/script.ts
```