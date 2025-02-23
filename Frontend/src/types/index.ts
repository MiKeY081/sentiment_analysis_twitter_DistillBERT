export interface Tweet {
  id: string;
  text: string;
  sentiment: 'positive' | 'negative' | 'neutral' | 'irrelevant';
  score: number;
}

export interface SentimentResults {
  distribution: 'positive' | 'negative' | 'neutral' | 'irrelevant';
  tweets: Tweet[];
}