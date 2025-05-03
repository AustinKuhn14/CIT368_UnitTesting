package src;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ValidateTest {
    @Test
    void testZip() {
        // Happy Path
        assertTrue(Validate.zip("17752"));
        assertFalse(Validate.zip("1775"));
        assertFalse(Validate.zip("009936"));

    }

    @Test
    void testMinor() {
        assertFalse(Validate.minor(18));
        assertTrue(Validate.minor(17));
        assertTrue(Validate.minor(16));
        assertTrue(Validate.minor(11));
        assertFalse(Validate.minor(1932));
        assertTrue(Validate.minor(0));
    }

    @Test
    void testEmail() {
        // Happy Path
        assertTrue(Validate.email("RandomName@example.com"));
        assertFalse(Validate.email("null.com"));
        assertFalse(Validate.email(""));

    }

    @Test
    void testIsLat() {
        assertTrue(Validate.isLat(12.34));
        assertFalse(Validate.isLat(98765.43));
    }

    @Test
    void testIsLng() {
        assertTrue(Validate.isLat(12.34));
        assertFalse(Validate.isLat(98765.43));
    }

    @Test
    void testIsDomain() {
        // Happy Path
        assertTrue(Validate.isDomain("somerandomweb.com"));

    }

    @Test
    void testIsInDomain() {
        assertTrue(Validate.isInDomain("somerandomweb.com", "test.somerandomweb.com"));
        assertFalse(Validate.isInDomain("somerandomweb.com", "test.somerandeb.com"));

    }

    @Test
    void testIsUrl() {
        assertTrue(Validate.isUrl("https://www.example.com"));
    }

    @Test
    void testGrade() {
        assertEquals('A', Validate.grade(90.0));
        assertEquals('A', Validate.grade(124.0));
        assertEquals('F', Validate.grade(0.0));
    }

    @Test
    void testIp() {
        assertTrue(Validate.ip("192.168.1.1"));
        assertFalse(Validate.ip("abcd.efgh.ijkl.mnop"));
        assertFalse(Validate.ip("192.168.1"));

    }

    @Test
    void testMac() {
        assertTrue(Validate.mac("00:1A:2B:3C:4D:5E"));
        assertFalse(Validate.mac("00:1G:2B:3C:4D:5E"));


    }

    @Test
    void testMd5() {
        assertTrue(Validate.md5("5d41402abc4b2a76b9719d911017c592"));
        assertFalse(Validate.md5("12345"));

    }
}