const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const FixStyleOnlyEntriesPlugin = require("webpack-fix-style-only-entries");

module.exports = () => {
  return {
    mode: 'production',
    entry: {
      'index': './app/resources/js/index.js',
      'style': './app/resources/scss/main.scss',
    },
    output: {
      path: path.resolve(__dirname, 'app/public/static'),
      filename: 'js/[name].bundle.min.js'
    },
    devServer: {
      contentBase: path.resolve(__dirname, './app/public/static'),
      hot: true
    },
    plugins: [
      new FixStyleOnlyEntriesPlugin(),
      new MiniCssExtractPlugin({
        filename: 'css/[name].min.css'
      }),
    ],
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: [
                '@babel/preset-env'
              ]
            }
          }
        },
        {
          test: /\.(s(a|c)ss)$/,
          exclude: /node_modules/,
          use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
            'sass-loader',
            {
              loader: 'sass-loader',
              options: {
                implementation: require("sass")
              }
            }
          ]
        }
      ]
    }
  }
};