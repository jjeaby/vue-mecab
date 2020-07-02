module.exports = {
    root: true,
    env: {
        node: true,
    },
    extends: [
        'plugin:vue/essential',
        '@vue/airbnb',
    ],
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'info' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'info' : 'off',
        'ter-indent': [
            true, 4, { SwitchCase: true },
        ],
        indent: ['error', 4],

    },
    parserOptions: {
        parser: 'babel-eslint',
    },
};
