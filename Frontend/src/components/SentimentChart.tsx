import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';

interface SentimentChartProps {
  distribution: {
    positive: number;
    negative: number;
    neutral: number;
    irrelevant: number;  // Adding irrelevant sentiment to the distribution
  };
}

export function SentimentChart({ distribution }: SentimentChartProps) {
  const data = [
    { name: 'Positive', value: distribution.positive},
    { name: 'Negative', value: distribution.negative },
    { name: 'Neutral', value: distribution.neutral },
    { name: 'Irrelevant', value: distribution.irrelevant },  // Include irrelevant
  ];

  // Ensure the data doesn't contain any undefined or NaN values.
  const filteredData = data.filter(item => !isNaN(item.value));

  const COLORS = ['#4caf50', '#f44336', '#ff9800', '#9e9e9e'];  // Add color for irrelevant

  return (
    <div className="w-full h-[400px]">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={filteredData}
            cx="50%"
            cy="50%"
            labelLine={false}
            outerRadius={150}
            dataKey="value"
            stroke="none"
          >
            {filteredData.map((_, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
