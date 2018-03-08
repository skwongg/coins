import React from 'react';
import { Card, Icon } from 'semantic-ui-react';
import { Link } from 'react-router-dom';

const AddCoinCTA = () => (
  <Card centered>
    <Card.Content textAlign="center">
      <Card.Header> Add a new coin to your hodls</Card.Header>
      <Link to="/coins/new"><Icon name="plus circle" size="massive"/></Link>
    </Card.Content>
  </Card>

)

export default AddCoinCTA;
