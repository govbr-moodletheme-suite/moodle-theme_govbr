export default [
    {
        files: ["usability_lab/**/*.js"],
        languageOptions: {
            ecmaVersion: "latest",
            sourceType: "script",
            globals: {
                document: "readonly",
                window: "readonly",
                localStorage: "readonly",
                Blob: "readonly",
                URL: "readonly",
            },
        },
        rules: {
            "no-unused-vars": [
                "error",
                { argsIgnorePattern: "^_", caughtErrorsIgnorePattern: "^_" },
            ],
            "no-undef": "error",
        },
    },
];
