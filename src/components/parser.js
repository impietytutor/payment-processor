/**
 * Payment processor parser.
 *
 * This module is responsible for parsing payment data from various sources.
 */

const { promisify } = require('util');
const { parseString } = require('xml2js');

const parseXml = promisify(parseString);

async function parsePaymentData(data) {
  try {
    const parsedData = await parseXml(data);
    return parsedData.root;
  } catch (error) {
    throw new Error(`Error parsing payment data: ${error.message}`);
  }
}

module.exports = { parsePaymentData };