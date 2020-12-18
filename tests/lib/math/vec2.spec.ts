import Vec2 from '@lib/math/vec2';

describe('Vec2', () => {
    it('should init as Zero', () => {
        const v = new Vec2();

        expect(v.x).toBe(0);
        expect(v.y).toBe(0);
    });

    it ('should add component wise', () => {
        const a = new Vec2(1, 2);
        const b = new Vec2(3, 4);

        const res = Vec2.add(a, b);

        expect(res.x).toBe(4);
        expect(res.y).toBe(6);
    });
});