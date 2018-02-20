import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { Route } from 'react-router-dom';
import HomePage from './components/pages/HomePage';


const App = ({location}) =>
  <div className="ui container">

    <Route location={location} path="/" exact component={HomePage}/>

  </div>

App.propTypes = {
  location: PropTypes.shape({
    pathname: PropTypes.string.isRequired
  }).isRequired,
  // isAuthenticated: PropTypes.bool.isRequired
}

function mapStateToProps(state){
  return {
    isAuthenticated: null
  }
}
export default connect(mapStateToProps)(App);
