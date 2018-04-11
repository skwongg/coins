import React from 'react';
import { Segment, Header } from 'semantic-ui-react';
import { LineChart } from 'react-easy-chart';



const CoinCard = ({coin}) => (
    <Segment>
      <Segment.Group horizontal>
        <Segment>
        <Header>
          {coin.pair}
        </Header>
      </Segment>
      <Segment>
        <Header>
          {coin.price}
        </Header>
      </Segment>
      </Segment.Group>
      <LineChart lineColors={['green']} width={400} height={40} data={[
          [
            {x: 1523429528, y: 384},
            {x: 1523430528, y: 385},
            {x: 1523431123, y: 407}
        ]
      ]}/>
    </Segment>
  )
export default CoinCard
