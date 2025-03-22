import { rubik_mono_one, silkscreen } from "@/lib/fonts";

/**
 * The Fraxation label for fonts
 *
 * @param {className}: The className for css 
 */
export function LogoLabelComp({ className }: { className?: string }) {
    return (
        <p className={className}>
            <span className={silkscreen.className}>FRA</span>
            <span className={rubik_mono_one.className}>X</span>
            <span className={silkscreen.className}>ATION</span>
        </p>
    );
}