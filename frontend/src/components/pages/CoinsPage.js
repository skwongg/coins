import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Grid, Image } from 'semantic-ui-react';
import { coins } from '../../actions/coins';


class CoinsPage extends React.Component {
  submit = (data) =>
    this.props.coins(data).then();



  render() {
    return (
      <Grid stackable columns={3} divided>

      </Grid>
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
