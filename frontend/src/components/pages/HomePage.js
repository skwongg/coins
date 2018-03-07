import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../../actions/auth'
import { Container } from 'semantic-ui-react';

const HomePage = ({ isAuthenticated, logout }) => (
  <Container>
    <h1>Home Page</h1>
    
  </Container>
)

HomePage.propTypes={
  isAuthenticated: PropTypes.bool.isRequired,
  logout: PropTypes.func.isRequired
}

function mapStateToProps(state){
  return {
    isAuthenticated: !!state.user.token
  }
};

export default connect(mapStateToProps, { logout })(HomePage)
