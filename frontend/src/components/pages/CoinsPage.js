import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Grid, Image, Segment } from 'semantic-ui-react';
import { coins } from '../../actions/coins';


class CoinsPage extends React.Component {
  submit = (data) =>
    this.props.coins(data).then();



  render() {
    return (
      <Segment stackable columns={3} divided>
        <Grid>
          abcabc
        </Grid>
      </Segment>
    )
  }
}



CoinsPage.propTypes = {
  isConfirmed: PropTypes.bool.isRequired
};

function mapStateToProps(state) {
  return {
    isConfirmed: !!state.user.confirmed
  };
}

export default connect(mapStateToProps)(CoinsPage);
