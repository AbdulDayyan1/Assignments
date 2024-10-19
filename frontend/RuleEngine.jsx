import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

const RuleEngine = () => {
  const [ruleName, setRuleName] = useState('');
  const [ruleString, setRuleString] = useState('');
  const [userData, setUserData] = useState('');
  const [ruleIds, setRuleIds] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const createRule = async () => {
    try {
      const response = await fetch('/api/rules', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: ruleName, rule_string: ruleString })
      });
      const data = await response.json();
      if (response.ok) {
        setError('');
        alert(`Rule created successfully with ID: ${data.id}`);
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('Failed to create rule');
    }
  };

  const evaluateRules = async () => {
    try {
      const response = await fetch('/api/evaluate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_data: JSON.parse(userData),
          rule_ids: ruleIds.split(',').map(id => parseInt(id.trim()))
        })
      });
      const data = await response.json();
      if (response.ok) {
        setResult(data.result);
        setError('');
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('Failed to evaluate rules');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Rule Engine</h1>
      
      <Card className="mb-4">
        <CardHeader>
          <CardTitle>Create Rule</CardTitle>
        </CardHeader>
        <CardContent>
          <Input
            className="mb-2"
            placeholder="Rule Name"
            value={ruleName}
            onChange={(e) => setRuleName(e.target.value)}
          />
          <Textarea
            className="mb-2"
            placeholder="Rule String (e.g. (age > 18) AND (income < 50000))"
            value={ruleString}
            onChange={(e) => setRuleString(e.target.value)}
          />
          <Button onClick={createRule}>Create Rule</Button>
        </CardContent>
      </Card>
      
      <Card className="mb-4">
        <CardHeader>
          <CardTitle>Evaluate Rules</CardTitle>
        </CardHeader>
        <CardContent>
          <Textarea
            className="mb-2"
            placeholder="User Data (JSON format)"
            value={userData}
            onChange={(e) => setUserData(e.target.value)}
          />
          <Input
            className="mb-2"
            placeholder="Rule IDs (comma-separated)"
            value={ruleIds}
            onChange={(e) => setRuleIds(e.target.value)}
          />
          <Button onClick={evaluateRules}>Evaluate Rules</Button>
        </CardContent>
      </Card>

      {result && <div className="mt-4">Result: {result.toString()}</div>}
      {error && <div className="mt-4 text-red-500">{error}</div>}
    </div>
  );
};

export default RuleEngine;
