'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const plugin = require('./index');

const tools = [];
plugin.apply({tool: definition => tools.push(definition)});
const manifest = JSON.parse(fs.readFileSync(path.join(__dirname, 'manifest.json'), 'utf8'));
assert.equal(manifest.id, 'office');
assert.equal(manifest.enabled, true);
assert.deepEqual(tools.map(t => t.name), ['office_document_search', 'office_document_read', 'office_document_edit', 'office_create', 'office_comments', 'office_comment_edit']);
assert.deepEqual(tools[3].parameters.required, ['path', 'format', 'content']);
const content = tools[3].parameters.properties.content;
assert.equal(content.additionalProperties, false);
assert.deepEqual(Object.keys(content.properties), ['title','blocks','sheets','slides']);
assert.deepEqual(content.properties.blocks.items.properties.type.enum,['heading','paragraph','table']);
assert.equal(content.properties.blocks.items.additionalProperties,false);
assert.equal(content.properties.sheets.items.properties.rows.items.type,'array');
assert.equal(content.properties.slides.items.properties.body.type,'string');
assert.throws(() => tools[3].handler({}), /原生工作区执行器/);
console.log('office plugin registration PASS');

assert.equal(manifest.settingsSchema,undefined,'Built-in Office must not require service settings');
assert.equal(manifest.tools.find(t=>t.name==='office_document_edit').kind,'write');
assert.deepEqual(tools[2].parameters.required,['path','hash','changes']);
