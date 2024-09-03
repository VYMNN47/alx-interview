#!/usr/bin/node
const request = require('request');

const filmNumber = process.argv[2];

if (!filmNumber) {
  console.error('Please provide a film number.');
  process.exit(1);
}

function fetchCharacterDetails (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      if (response.statusCode === 200) {
        try {
          const data = JSON.parse(body);
          resolve(data.name);
        } catch (e) {
          reject(e);
        }
      } else {
        reject(new Error('Response Status: ' + response.statusCode));
      }
    });
  });
}

function fetchCharacters (data) {
  const characterList = data.characters;
  const characterPromises = characterList.map(fetchCharacterDetails);

  Promise.all(characterPromises)
    .then(characterNamesList => {
      characterNamesList.forEach(name => {
        console.log(name);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

const url = `https://swapi-api.alx-tools.com/api/films/${filmNumber}`;
request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
    return;
  }
  if (response.statusCode === 200) {
    try {
      const data = JSON.parse(body);
      fetchCharacters(data);
    } catch (e) {
      console.error('Error parsing film JSON:', e);
    }
  } else {
    console.log('Response Status:', response.statusCode);
  }
});
