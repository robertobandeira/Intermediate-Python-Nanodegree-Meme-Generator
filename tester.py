from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.TXTIngestor import TXTIngestor

print(CSVIngestor.parse('_data/DogQuotes/dogQuotesCSV.csv'))
print(TXTIngestor.parse('_data/DogQuotes/dogQuotesTXT.txt'))