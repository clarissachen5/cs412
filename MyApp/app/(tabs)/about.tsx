import { Text, View } from '@/components/Themed';
import { styles } from '../../assets/my_styles';

export default function AboutScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>About</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
    </View>
  );
}