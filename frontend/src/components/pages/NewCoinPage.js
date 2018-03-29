import React from 'react';
import { Segment } from 'semantic-ui-react';
import CoinForm from '../forms/CoinForm';
import SearchCoinForm from '../forms/SearchCoinForm';


class NewCoinPage extends React.Component{
  state = {
    coin: null
  }

  onCoinSelect = coin => {
    this.setState({ coin });
  }


  render() {
    return (

      <Segment>
        <h1>Search for a new coin to add.</h1>
        <SearchCoinForm onCoinSelect={this.onCoinSelect}/>
        {this.state.coin && <CoinForm submit={this.addCoin} coin={this.state.coin}/>}
      </Segment>
    )
  }
}

export default NewCoinPage
