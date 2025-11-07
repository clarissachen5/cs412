import { StyleSheet } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import { styles } from '../../assets/my_styles';

export default function DetailScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Detail</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
    </View>
  );
}
