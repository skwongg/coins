import React from 'react';
import { Segment } from 'semantic-ui-react';
import SearchCoinForm from '../forms/SearchCoinForm';

class NewCoinPage extends React.Component{
  state = {
    coin: null
  }

  render() {
    return (

      <Segment>
        <h1>Search for a new coin to add.</h1>
        <SearchCoinForm/>
      </Segment>
    )
  }
}

export default NewCoinPage
