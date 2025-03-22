const path = require('path');

module.exports = {
  entry: 'floran/static/js/main.js', // Point d'entrée du bundle
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        parser: { sourceType: 'module' }, // Forcer le parsing en tant que module
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
            // Vous pouvez aussi ajouter "sourceType: 'module'" ici si nécessaire
          },
        },
      },
    ],
  },
  mode: 'production', // Passez en "production" pour la version finale
};