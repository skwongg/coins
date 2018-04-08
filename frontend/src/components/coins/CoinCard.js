import React from 'react'
import { Segment } from 'semantic-ui-react';

const CoinCard = ({coin}) => (
  // { coin } = this.props
    <Segment>{coin.pair}</Segment>
  )
export default CoinCard
