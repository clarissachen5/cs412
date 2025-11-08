// File: MyApp/assets/my_styles.ts
// Author: Clarissa Chen (clchen5@bu.edu), 11/7/2025
// Description: Specifies styling for MyApp

import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: "lightblue",
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  subText: {
    fontSize: 16,
    textAlign: "center",
    padding: 20,
    
  },
  citiesText: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: "center",
    padding: 20,
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});