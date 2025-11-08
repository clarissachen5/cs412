// File: MyApp/app/(tabs)/index.tsx
// Author: Clarissa Chen (clchen5@bu.edu), 11/7/2025
// Description: Displays the index page

import { StyleSheet, Image} from 'react-native';
import { Text, View } from '@/components/Themed';
import { styles } from '../../assets/my_styles';

const profileImg = require("../../assets/images/linkedin profile copy.jpeg");

export default function IndexScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Clarissa Chen</Text>
            <Text style={styles.subText}>Risk-taking community builder who executes</Text>
       <Image source={profileImg} style={{ width: 300, height: 300 }} />

      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      {/* <EditScreenInfo path="app/(tabs)/index.tsx" /> */}
    </View>
  );
}
