const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });
var express = require('express')
const fs = require('fs');
const config = require('./config.json')
var cors = require('cors')

var app = express()

app.use(cors())

const TOKEN = config.token

client.login(TOKEN);

app.get('/favicon.ico', (req, res) => res.status(204));

app.get('/userValidation/:uid', (req, res) => {
    var id = req.params.uid
    client.users.fetch(id).then(async (user) => {
        res.send(user)
    }).catch(async (err) => {
        res.send({id: null})
    })
})

app.get('/drop', (req, res) => {
    var sys   = require('util'),
    spawn = require('child_process').spawn,
    dummy = spawn('python', ['./python_scripts/drop_cards.py']);

    dummy.stdout.on('data', function(data) {
        var _data = JSON.parse(data.toString().replaceAll("'", '"'))
        res.json(_data)
    });
})

app.listen('8081')